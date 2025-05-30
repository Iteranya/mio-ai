from dataclasses import dataclass

@dataclass
class DailyEntry:
    id:str
    raw_text:str
    csv:str
    report:str
    created:int
    updated:int
    error: str

@dataclass
class FinanceBook:
    id:str
    title:str
    description:str
    read_perm:list[str]
    edit_perm:list[str]
    gsheet_link: str
