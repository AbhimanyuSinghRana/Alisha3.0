# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# @Venom_Hai_Hum 
# Owner AbhimanyuSinghRana 

from typing import Dict
from typing import List


admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> List[int]:
    if chat_id in admins:
        return admins[chat_id]
    return []
