class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_url: str = homepage
        # Ordered from oldest (left) to newest (right)
        self.back_stack: list[str] = []
        # Ordered from oldest (left) to ewest (right)
        self.forward_stack: list[str] = []


    def visit(self, url: str) -> None:
        self.forward_stack = []
        self.back_stack.append(self.current_url)
        self.current_url = url
        

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.back_stack))
        if steps > 0:
            urls_to_forward = self.back_stack[len(self.back_stack)-steps+1:] + [self.current_url]
            self.forward_stack = urls_to_forward + self.forward_stack
            self.current_url = self.back_stack[len(self.back_stack)-steps]
            self.back_stack = self.back_stack[:len(self.back_stack)-steps]
        return self.current_url
        

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.forward_stack))
        if steps > 0:
            urls_to_back = [self.current_url] + self.forward_stack[:steps-1]
            self.back_stack = self.back_stack + urls_to_back
            self.current_url = self.forward_stack[steps-1]
            self.forward_stack = self.forward_stack[steps:]
        return self.current_url



# Your BrowserHistory object will be instantiated and called as such:
homepage = "google.com"
obj = BrowserHistory(homepage)
assert obj.current_url == homepage
assert not bool(obj.back_stack)
assert not bool(obj.forward_stack)
obj.visit("marca.com")
assert obj.current_url == "marca.com"
assert obj.back_stack == [homepage]
assert not bool(obj.forward_stack)
obj.visit("facebook.com")
assert obj.current_url == "facebook.com"
assert obj.back_stack == [homepage, "marca.com"]
assert not bool(obj.forward_stack)
obj.visit("amazon.com")
assert obj.current_url == "amazon.com"
assert obj.back_stack == [homepage, "marca.com", "facebook.com"]
assert not bool(obj.forward_stack)
param_2 = obj.back(2)
print(obj.back_stack)
print(obj.forward_stack)
assert param_2 == "marca.com"
assert obj.current_url == "marca.com"
assert obj.back_stack == [homepage]
assert obj.forward_stack == ["facebook.com", "amazon.com"]
param_3 = obj.forward(1)
print(obj.back_stack)
print(obj.forward_stack)
assert param_3 == "facebook.com"
assert obj.current_url == "facebook.com"
assert obj.back_stack == [homepage, "marca.com"]
assert obj.forward_stack == ["amazon.com"]
param_4 = obj.back(3)
print(obj.back_stack)
print(obj.forward_stack)
assert param_4 == homepage
assert obj.current_url == homepage
assert not bool(obj.back_stack)
assert obj.forward_stack == ["marca.com", "facebook.com", "amazon.com"]
param_5 = obj.back(1)
print(obj.back_stack)
print(obj.forward_stack)
assert param_5 == homepage
assert obj.current_url == homepage
assert not bool(obj.back_stack)
assert obj.forward_stack == ["marca.com", "facebook.com", "amazon.com"]
