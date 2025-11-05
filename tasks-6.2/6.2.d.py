import pandas as pd


def cheque(price_list, **purchases):
    df = pd.DataFrame({
        'product': list(purchases),
        'price': [price_list[p] for p in purchases],
        'number': list(purchases.values()),
        'cost': [price_list[p] * n for p, n in purchases.items()]
    })
    df = df.sort_values('product').reset_index(drop=True)
    return df

def discount(df):
    result = df.copy()
    # выбираем продукты кол-ва > 2, берем их итоговый кост
    # заменяем его новым со скидкой
    result.loc[result['number'] > 2, 'cost'] = result.loc[result['number'] > 2, 'cost'] * 0.5
    return result