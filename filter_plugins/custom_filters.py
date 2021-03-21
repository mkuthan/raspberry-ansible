class FilterModule(object):
    def filters(self):
        return {
            'select_attribute_by_key': self.select_attribute_by_key
        }

    @staticmethod
    def select_attribute_by_key(xs, key, value, attribute):
        elements = filter(lambda x: x[key] == value, xs)
        attributes = map(lambda x: x[attribute], elements)
        return next(attributes)
