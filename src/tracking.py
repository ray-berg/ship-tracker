import re
from dataclasses import dataclass
from typing import Optional, List

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


def parse_tracking_numbers(text: str) -> List[str]:
    """Parse user input into a list of tracking numbers."""
    numbers: List[str] = []
    for line in text.splitlines():
        for token in line.split(','):
            token = token.strip()
            if token:
                numbers.append(token)
    return numbers


_COURIER_LINKS = {
    "UPS": "https://www.ups.com/track?tracknum={}",
    "USPS": "https://tools.usps.com/go/TrackConfirmAction?tLabels={}",
    "FedEx": "https://www.fedex.com/fedextrack/?tracknumbers={}",
    "DHL": "https://www.dhl.com/en/express/tracking.html?AWB={}",
}


def get_courier_link(courier: str, tracking_number: str) -> Optional[str]:
    """Return a URL to the courier's website for the given number."""
    template = _COURIER_LINKS.get(courier)
    if not template:
        return None
    return template.format(tracking_number)


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
