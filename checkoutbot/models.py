import inspect
import sys
from typing import Dict, List, Type


RegisterType = Dict[int, List[int]]


class BaseModel:
    """
    Base class for creating other models.
    """

    def __init__(self, register_count: int):
        self.register_count = register_count
        self.registers: RegisterType = {i: [] for i in range(self.register_count)}
        self.customer_register_assignments: Dict[int, int] = {}
        self.total_item_count = 0
        self.customer_items: Dict[int, List[int]] = {}

    def clear(self):
        self.registers = {i: [] for i in range(self.register_count)}
        self.customer_register_assignments = {}

    def _select_register(self, customer_id: int) -> int:
        """
        Select a register to use for new customers.
        """
        register_items = self.registers.items()
        lowest_portion = 1
        lowest_key = None
        if not self.total_item_count:
            lowest_key = 0

        else:
            for key, value in register_items:
                portion = len(value) / self.total_item_count
                if portion < lowest_portion:
                    lowest_portion = portion
                    lowest_key = key
        self.customer_register_assignments[customer_id] = lowest_key
        return self.customer_register_assignments[customer_id]

    def add(self, customer_id: int, item_id: int):
        """
        Add an item to a register using the following rules:
            - If the customer already has items on a register, select that register.
            - If the customer is new, select a register using the model.
        """
        self._select_register(customer_id)
        register = self.customer_register_assignments[customer_id]
        self.registers[register].append(item_id)
        if customer_id not in self.customer_items.keys():
            self.customer_items[customer_id] = []
        self.customer_items[customer_id].append(item_id)
        self.total_item_count += 1
        return register

    def checkout(self, customer_id: int):
        cust_reg = self.customer_register_assignments[customer_id]
        for item in self.customer_items[customer_id]:
            for register_item in self.registers[cust_reg]:
                if register_item == item:
                    self.registers[cust_reg].remove(item)
                    self.total_item_count -= 1
                    break

    @staticmethod
    def get_model(model_name: str) -> Type["BaseModel"]:
        """
        Search this module for a subclass of BaseModel with a name that matches the given model name.
        """
        matches = (
            cls
            for name, cls in inspect.getmembers(
                object=sys.modules[__name__], predicate=inspect.isclass
            )
            if issubclass(cls, BaseModel) and name == model_name
        )
        cls = next(matches, None)
        if not cls:
            raise TypeError(
                f"{model_name} is not a subclass of BaseModel or it does not exist."
            )
        return cls
