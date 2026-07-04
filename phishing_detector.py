import re

class PhishingDetector:
    def __init__(self, email):
        self.email = email
        self.red_flags = []

    def check_sender_domain(self):
        # Red Flag 1: Sender-Domain Mismatch
        if not self.email['from'].endswith("@company.com"):
            self.red_flags.append("Suspicious sender domain")

    def check_subject_urgency(self):
        # Red Flag 5: Urgent Bypass Requests
        urgent_keywords = ["URGENT", "IMMEDIATE", "ACTION REQUIRED", "CONFIDENTIAL"]
        if any(word in self.email['subject'].upper() for word in urgent_keywords):
            self.red_flags.append("Urgency trigger detected")

    def check_links(self):
        # Red Flag: Lookalike domains (typosquatting, combosquatting)
        suspicious_patterns = [
            r"amaz0n\.com", r"paypal\.co", r"secure-login", r"update-billing"
        ]
        for link in self.email['links']:
            if any(re.search(pattern, link) for pattern in suspicious_patterns):
                self.red_flags.append(f"Suspicious link detected: {link}")

    def check_attachments(self):
        # Red Flag 4: Dangerous Attachments
        dangerous_extensions = [".iso", ".js", ".scr", ".exe"]
        for attachment in self.email['attachments']:
            if any(attachment.endswith(ext) for ext in dangerous_extensions):
                self.red_flags.append(f"Malicious attachment: {attachment}")

    def analyze(self):
        self.check_sender_domain()
        self.check_subject_urgency()
        self.check_links()
        self.check_attachments()

        if not self.red_flags:
            return "Safe email ✅"
        else:
            return f"Phishing suspected ⚠️\nRed Flags: {self.red_flags}"


# Example usage
email_example = {
    "from": "ceo.urgent@executive-update.com",
    "subject": "IMMEDIATE ACTION REQUIRED: Transfer Authorization",
    "links": ["http://secure-login.company-update.com"],
    "attachments": ["transfer_instructions.iso"]
}

detector = PhishingDetector(email_example)
result = detector.analyze()
print(result)
