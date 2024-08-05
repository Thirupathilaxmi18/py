# def get_full_name(first_name, last_name):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name
#
#
# print(get_full_name("john", "doe"))
# def fullname(fstname="laxmi",lastname="sangepu"):
#     return fstname.title()+" "+lastname.title()
# #print(fullname("ThirupATHI laxmi","sangepu"))
# print(fullname())
# def get_name_with_age(name: str, age: int):
#      return f"{name} is this old: {age}"
# print(get_name_with_age("laxmi",22))
# def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
#     return item_a, item_b, item_c, item_d, item_e
# print(get_items("laxmi",30,22.3,True,(2,3,4,5)))
# def process_items(items: list[str]):
#     for item in items:
#         print(item)
# process_items("laxmi")
# def process_items(items_t: tuple[int,int, str], items_s: set[bytes]):
#     return items_t, items_s
# print(process_items((20,20,"laxmi",50),{(1,2,3,4)}))
# def dict_fn(items_l: list[int,str,int],items_d: dict[str,int]):
#     return items_l,items_d
# print(dict_fn([6,"laxmi",7],{"laxmi":"name",2024:22}))
from typing import Union
def process_item(item: typing.Union(int,str)):
    print(item)
process_item(18 ,"laxmi")
