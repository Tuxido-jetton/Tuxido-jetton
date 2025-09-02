"""
Unified Tuxido Mining Bot Configuration
Integrates settings for both local and remote repositories
"""

import os
from typing import Dict, Any

class ProjectConfig:
    """Unified configuration manager for Tuxido Mining Bot"""

    def __init__(self):
        self.config = self._load_unified_config()

    def _load_unified_config(self) -> Dict[str, Any]:
        """Load unified configuration from environment and defaults"""
        return {
            # Project Identity
            "project": {
                "name": "TuxidoMineBot",
                "version": "2.0.0",
                "description": "AI-Powered TON Blockchain Mining Bot",
                "repository": "https://replit.com/@s9igma/TuxidoMineBot",
                "integrated_with": "Current Repl Instance",
                "ai_managed": True
            },

            # Mining Configuration
            "mining": {
                "min_hash_rate": int(os.getenv("MIN_HASH_RATE", "1")),
                "max_hash_rate": int(os.getenv("MAX_HASH_RATE", "10")),
                "log_interval": int(os.getenv("LOG_INTERVAL", "100")),
                "mining_delay": float(os.getenv("MINING_DELAY", "1.0")),
                "auto_optimize": os.getenv("AUTO_OPTIMIZE", "true").lower() == "true"
            },

            # TON Blockchain Configuration
            "blockchain": {
                "network": os.getenv("TON_NETWORK", "mainnet"),
                "wallet_address": os.getenv("TON_WALLET_ADDRESS", ""),
                "private_key": os.getenv("TON_PRIVATE_KEY", ""),
                "rpc_endpoint": os.getenv("TON_RPC_ENDPOINT", ""),
                "explorer_url": "https://tonscan.org"
            },

            # StonFi DEX Configuration
            "stonfi": {
                "enabled": os.getenv("STONFI_ENABLED", "true").lower() == "true",
                "jetton_address": os.getenv("TUXIDO_JETTON_ADDRESS", ""),
                "auto_trade": os.getenv("STONFI_AUTO_TRADE", "false").lower() == "true",
                "trade_percentage": float(os.getenv("STONFI_TRADE_PERCENT", "10")),
                "api_endpoint": os.getenv("STONFI_API", "https://api.ston.fi/v1"),
                "router_address": "EQB3ncyBUTjZUA5EnFKR5_EnOMI9V1tTEAAPaiU71gc4TiUt"
            },

            # Telegram Integration
            "telegram": {
                "bot_token": os.getenv("TELEGRAM_BOT_TOKEN", ""),
                "chat_id": os.getenv("TELEGRAM_CHAT_ID", ""),
                "notifications_enabled": os.getenv("TELEGRAM_NOTIFICATIONS", "false").lower() == "true",
                "update_interval": int(os.getenv("TELEGRAM_UPDATE_INTERVAL", "3600"))
            },

            # P2E Configuration
            "p2e": {
                "rewards_per_block": int(os.getenv("REWARDS_PER_BLOCK", "10")),
                "bonus_multiplier": float(os.getenv("BONUS_MULTIPLIER", "1.0")),
                "daily_limit": int(os.getenv("DAILY_LIMIT", "10000")),
                "streak_bonus": float(os.getenv("STREAK_BONUS", "1.1")),
                "achievement_system": os.getenv("ACHIEVEMENT_SYSTEM", "true").lower() == "true"
            },

            # AI Assistant Configuration
            "ai": {
                "enabled": os.getenv("OPENAI_API_KEY", "") != "",
                "model": os.getenv("AI_MODEL", "gpt-4"),
                "max_tokens": int(os.getenv("AI_MAX_TOKENS", "2000")),
                "temperature": float(os.getenv("AI_TEMPERATURE", "0.3")),
                "upgrade_interval": int(os.getenv("AI_UPGRADE_INTERVAL", "1800")),
                "monitoring_interval": int(os.getenv("AI_MONITORING_INTERVAL", "120")),
                "auto_commit": os.getenv("AI_AUTO_COMMIT", "true").lower() == "true",
                "optimization_enabled": os.getenv("AI_OPTIMIZATION", "true").lower() == "true"
            },

            # Security Configuration
            "security": {
                "enable_encryption": os.getenv("ENABLE_ENCRYPTION", "true").lower() == "true",
                "api_rate_limit": int(os.getenv("API_RATE_LIMIT", "100")),
                "max_daily_transactions": int(os.getenv("MAX_DAILY_TX", "10000")),
                "backup_enabled": os.getenv("BACKUP_ENABLED", "true").lower() == "true"
            },

            # Performance Configuration
            "performance": {
                "concurrent_miners": int(os.getenv("CONCURRENT_MINERS", "1")),
                "memory_limit_mb": int(os.getenv("MEMORY_LIMIT_MB", "512")),
                "cpu_limit_percent": int(os.getenv("CPU_LIMIT_PERCENT", "80")),
                "disk_space_threshold_mb": int(os.getenv("DISK_THRESHOLD_MB", "100"))
            },

            # Logging Configuration
            "logging": {
                "level": os.getenv("LOG_LEVEL", "INFO"),
                "file_enabled": os.getenv("LOG_FILE_ENABLED", "true").lower() == "true",
                "max_log_size_mb": int(os.getenv("MAX_LOG_SIZE_MB", "10")),
                "backup_count": int(os.getenv("LOG_BACKUP_COUNT", "5"))
            }
        }

    def get(self, section: str, key: str = None, default: Any = None) -> Any:
        """Get configuration value"""
        if key is None:
            return self.config.get(section, default)
        return self.config.get(section, {}).get(key, default)

    def update(self, section: str, key: str, value: Any) -> None:
        """Update configuration value"""
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value

    def is_ai_enabled(self) -> bool:
        """Check if AI features are enabled"""
        return self.get("ai", "enabled", False)

    def is_production_ready(self) -> bool:
        """Check if configuration is ready for production"""
        required_configs = [
            ("blockchain", "wallet_address"),
            ("blockchain", "network")
        ]

        for section, key in required_configs:
            if not self.get(section, key):
                return False
        return True

    def get_mining_config(self) -> Dict[str, Any]:
        """Get mining configuration"""
        return self.get("mining", default={})

    def get_ai_config(self) -> Dict[str, Any]:
        """Get AI configuration"""
        return self.get("ai", default={})

    def get_blockchain_config(self) -> Dict[str, Any]:
        """Get blockchain configuration"""
        return self.get("blockchain", default={})

# Global configuration instance
config = ProjectConfig()