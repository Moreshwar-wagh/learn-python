def car_info(manufacture, model, color):
    """Dictionary About Car"""
    info = {"Manufacture": manufacture, "Model": model, "Features": color}
    print(f"\n Car Information: {info}")
    return info


about_car = car_info('Toyota', 'Fortuner', 'Color:White')
about_car = car_info('Ford', 'Mustang', 'Color:Yellow')
about_car = car_info('Chevrolet', 'Cruse', 'Color:Black')
about_car = car_info('Maruti', 'Swift', 'Color:Red')
