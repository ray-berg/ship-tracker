import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class TrackingInfo:
    courier: str
    status: str


def detect_courier(tracking_number: str) -> Optional[str]:
    """Return the courier code based on tracking number format."""
    tn = tracking_number.strip()
    if re.fullmatch(r"1Z[0-9A-Z]{16}", tn):
        return "UPS"
    if re.fullmatch(r"\d{22}", tn):
        return "USPS"
    if re.fullmatch(r"\d{12}", tn):
        return "FedEx"
    if re.fullmatch(r"\d{10}", tn):
        return "DHL"
    return None


# sample status database
_STATUS_DB = {
    "1Z9999999999999999": "Delivered",
    "9400110200881111111111": "In transit",
    "123456789012": "Label created",
    "1234567890": "Out for delivery",
}


def fetch_status(tracking_number: str) -> Optional[TrackingInfo]:
    """Return TrackingInfo for known tracking numbers."""
    courier = detect_courier(tracking_number)
    if not courier:
        return None
    status = _STATUS_DB.get(tracking_number.strip(), "Unknown")
    return TrackingInfo(courier=courier, status=status)
