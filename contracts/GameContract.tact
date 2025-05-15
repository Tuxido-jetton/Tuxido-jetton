contract GameContract {
        address owner;
            int level;
                int lockedTokens;

                    init(owner: address) {
                                self.owner = owner;
                                        self.level = 1;
                                                self.lockedTokens = 0;
                    }

                        receive("lock") {
                                    // Locking tokens increases level
                                            self.lockedTokens += msg.value;
                                                    self.level += 1;
                        }

                            receive("get_status") {
                                        send(msg.sender, "status", slice{
                                                        level: self.level,
                                                                    locked: self.lockedTokens
                                        });
                            }
}
                                        })
                            }
                        }
                    }
}