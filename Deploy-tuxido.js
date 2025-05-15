import { TonClient, WalletContractV4, internal, fromNano, toNano } from "ton";
import { mnemonicToWalletKey } from "ton-crypto";
import { JettonMinter } from "ton-jetton";

// Replace with your 24-word mnemonic
const MNEMONIC = "replace this with your 24-word seed phrase";

async function main() {
    const client = new TonClient({ endpoint: "https://toncenter.com/api/v2/jsonRPC" });

    // Load wallet key from mnemonic
    const key = await mnemonicToWalletKey(MNEMONIC);
    const wallet = WalletContractV4.create({ publicKey: key.publicKey, workchain: 0 });
    const walletAddress = wallet.address;
    console.log("Wallet address:", walletAddress.toFriendly());

    // Open wallet
    const walletContract = client.open(wallet);
    const balance = await walletContract.getBalance();
    console.log("Wallet balance:", fromNano(balance), "TON");

    // Prepare Jetton Minter
    const jetton = JettonMinter.create({
        owner: walletAddress,
        content: {
            type: 'offchain',
            uri: "https://yourdomain.com/metadata.json" // Replace with your token's metadata
        },
        admin: walletAddress
    });

    const jettonAddress = jetton.address;
    console.log("Jetton address will be:", jettonAddress.toFriendly());

    // Send deployment message
    const seqno = await walletContract.getSeqno();
    await walletContract.sendTransfer({
        seqno,
        secretKey: key.secretKey,
        messages: [
            internal({
                to: jettonAddress,
                value: toNano("0.05"),
                bounce: false,
                body: jetton.createDeployBody()
            }),
        ]
    });

    console.log("Deployment message sent!");
}

main().catch(console.error);
