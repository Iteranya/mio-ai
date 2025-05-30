from dataclasses import dataclass

@dataclass
class DailyEntry:
    id:str
    raw_text:str
    csv:str
    notes:str
    created:int
    updated:int
    error: str


