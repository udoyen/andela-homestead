def calculate_tax(taxinfo):
    tax = 0
    newtax = 0
    info = {}
    if not isinstance(taxinfo, int):
        if taxinfo:
            for key, value in taxinfo.items():
                if not isinstance(value, str):
                    if isinstance(value, int):
                        if value < 1000:
                            tax = 0
                            info[key] = tax
                        else:
                            if value > 1000.0:
                                value -= 1000.0
                                tax = 0
                                if value > 9000:
                                    value -= 9000
                                    newtax = float((10.0 / 100.0) * 9000)
                                    tax += newtax
                                    if value > 10200:
                                        value -= 10200
                                        newtax = float((15.0 / 100.0) * 10200)
                                        tax += newtax
                                        if value > 10550:
                                            value -= 10550
                                            newtax = float((20.0 / 100.0) * 10550)
                                            tax += newtax
                                            if value > 19250:
                                                value -= 19250
                                                newtax = float((25.0 / 100.0) * 19250)
                                                tax += newtax
                                                if value > 50000:
                                                    newtax = float((30.0 / 100.0) * value)
                                                    tax += newtax
                                                    info[key] = tax
                                                else:
                                                    newtax = (float((30.0 / 100.0) * value))
                                                    tax += newtax
                                                    info[key] = tax
                                            else:
                                                newtax = (float((25.0 / 100.0) * value))
                                                tax += newtax
                                                info[key] = tax
                                        else:
                                            newtax = (float((20.0 / 100.0) * value))
                                            tax += newtax
                                            info[key] = tax
                                    else:
                                        newtax = (float((15.0 / 100.0) * value))
                                        tax += newtax
                                        info[key] = tax
                                else:
                                    newtax = (float((10.0 / 100.0) * value))
                                    tax += newtax
                                    info[key] = tax
                    else:
                        raise ValueError()
                else:
                    raise ValueError()
            return info
        else:
            return taxinfo
    else:
        raise ValueError()


print(calculate_tax({"James": 20500}))
