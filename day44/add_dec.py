def add_role(func):
    def add_parameter(*args,**kwargs):
        kwargs["role"]="admin"
        return func(*args,**kwargs)
    return add_parameter


@add_role

def show_user(name, role):
    print("Role:", role)
    print("Name:", name)

show_user("Goutham")