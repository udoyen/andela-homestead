def calculate_tax(taxinfo):
    tax = 0
    newtax = 0
    info = {}
    if isinstance(taxinfo, dict):
        for key, value in taxinfo.items():
            if value < 1000:
                tax = 0
                info[key] = tax
            else:
                if value > 1000:
                    value -= 1000
                    tax = 0
                if value > 9000:
                    value -= 9000
                    newtax = (10 / 100) * 9000
                    tax += newtax
                else:
                    newtax = ((10 / 100) * value)
                    tax += newtax
                    info[key] = tax
                if value > 10200:
                    value -= 10200
                    newtax = (15 / 100) * 10200
                    tax += newtax
                else:
                    newtax = ((15 / 100) * value)
                    tax += newtax
                    info[key] = tax
                if value > 10550:
                    value -= 10550
                    newtax = (20 / 100) * 10550
                    tax += newtax
                else:
                    newtax = ((20 / 100) * value)
                    tax += newtax
                    info[key] = tax
                if value > 19250:
                    value -= 19250
                    newtax = (25 / 100) * 19250
                    tax += newtax
                else:
                    newtax = ((25 / 100) * value)
                    tax += newtax
                    info[key] = tax
                if value > 50000:
                    newtax = (30 / 100) * value
                    tax += newtax
                    info[key] = tax
                else:
                    newtax = ((30 / 100) * value)
                    tax += newtax
                    info[key] = tax
    else:
        return "Only dictionaries are allowed"
    return info


print(calculate_tax({'Alex': 500, 'James': 20500, 'Kinuthia': 70000}))
