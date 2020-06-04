from .. import datasources


def test_limits_settings():
    limits_settings = {
        "default": {
            "Residential": {
                "city1": 100,
                "city2": 200
            },
        }, "foo": {
            "Residential": {
                "city1": 50
            },
            "Office": {
                "city3": 12
            }
        }
    }
    out = datasources.limits_settings({"development_limits": limits_settings},
                                      "foo")
    assert out["Residential"]["city1"] == 50
    assert out["Residential"]["city2"] == 200
    assert out["Office"]["city3"] == 12


def test_inclusionary_housing_settings():
    inclusionary_housing_settings = {
        "foo": [{
            "amount": .2,
            "values": [
                "Berkeley",
                "Oakland"
            ]
        }, {
            "amount": .1,
            "values": [
                "San Francisco"
            ]
        }]
    }
    inclusionary_housing_settings_fr2 = {
        "foo": [{
            "amount": .2,
            "values": [
                "Berkeley",
                "Oakland"
            ]
        }, {
            "amount": .1,
            "values": [
                "San Francisco"
            ]
        }]
    }
    inclusionary_housing_settings_d_b = {
        "foo": [{
            "amount": .2,
            "values": [
                "Berkeley",
                "Oakland"
            ]
        }, {
            "amount": .1,
            "values": [
                "San Francisco"
            ]
        }]
    }
    out = datasources.inclusionary_housing_settings({
        "inclusionary_housing_settings": inclusionary_housing_settings
    }, "foo")
    out_fr2 = datasources.inclusionary_housing_settings_fr2({
        "inclusionary_housing_settings_fr2": inclusionary_housing_settings_fr2
    }, "foo")
    out_d_b = datasources.inclusionary_housing_settings_d_b({
        "inclusionary_housing_settings_d_b": inclusionary_housing_settings_d_b
    }, "foo")

    assert ((out["Berkeley"] == .2) or (out_fr2["Berkeley"] == .2) or (out_d_b["Berkeley"] == .2))
    assert ((out["Oakland"] == .2) or (out_fr2["Oakland"] == .2) or (out_d_b["Oakland"] == .2))
    assert ((out["San Francisco"] == .1) or (out_fr2["San Francisco"] == .1) or (out_d_b["San Francisco"] == .1))
