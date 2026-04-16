def test_header_present(dash_duo):
    from app import app
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualiser"

def test_chart_present(dash_duo):
    from app import app
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    assert dash_duo.find_element("#sales-chart") is not None

def test_region_picker_present(dash_duo):
    from app import app
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-radio", timeout=10)
    assert dash_duo.find_element("#region-radio") is not None
