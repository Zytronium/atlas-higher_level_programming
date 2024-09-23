from models.rectangle import Rectangle

if __name__ == "__main__":
    r = Rectangle(10, 4, 0, 1)
    print(r.id, r.width)
    r.update(id=5, width=12, hawiuhdiufha=53, height=10)
    print(r.id, r.width)
    rstr = r.to_json_string([r.to_dictionary()])
    # r2 = Rectangle(12, 10, 0, 0, 4)
    r2d2 = Rectangle.create(**(Rectangle.from_json_string(rstr)[0]))
    print(r)
    print(r2d2)
    print(r == r2d2)
