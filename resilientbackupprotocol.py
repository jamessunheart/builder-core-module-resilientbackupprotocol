import time
from typing import Dict, List

class ResilientBackupProtocol:
    def __init__(self):
        self.backup_log: List[Dict] = []
        self.alert_threshold = 3  # e.g., modules uncommitted or at risk

    def record_backup(self, location: str, modules: List[str]):
        self.backup_log.append({
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
            "location": location,
            "modules": modules
        })

    def notify_founder(self, reason: str):
        print(f"ALERT: James Sunheart — action needed: {reason}")
        print("You may restore from latest encrypted backup. Guide will be provided.")

    def trigger_backup(self, modules: List[str], location: str):
        print(f"Backing up to {location}...")
        self.record_backup(location, modules)
        print("Backup complete.")

    def check_backup_health(self, module_status: Dict[str, bool]):
        at_risk = [m for m, ok in module_status.items() if not ok]
        if len(at_risk) >= self.alert_threshold:
            self.notify_founder("Multiple critical modules are unbacked or unstable.")

    def guide_restore(self):
        print("To restore Builder Core:")
        print("1. Access secure backup vault.")
        print("2. Decrypt with founder key.")
        print("3. Import module bundle into system core.")
        print("4. Confirm system heartbeat and resume ops.")