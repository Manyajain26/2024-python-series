class Employee:

    def __init__(self, name: str, id: int, devices: list[str]) -> None:
        self.name = name
        self.id = id
        self.devices = devices

    def package(self, salary):
        self.salary = salary
        print(f'Yearly salary={salary * 12} INR')

    def raise_amount(self):
        raise_ratio = 2
        print(f'New salary={self.salary * raise_ratio}')

    def totlitems(self):
        print(f' {self.name} have these Devices={self.devices}')
        print(f'total items= {len(self.devices)}')


emp1 = Employee("manya", 26, ["mac", "mouse"])
emp1.package(80000)
emp1.raise_amount()
emp1.totlitems()
