# Create your pytest cases here
from src.shipment_pairs import remove_intra, collect_pairs

def test_remove_intra():
    shipments = [
        ['IN', 'US', 8],
        ['US', 'US', 14],
        ['IN', 'CA', 3],
        ['IN', 'IN', 13],
        ['CA', 'CA', 16],
    ]

    result = remove_intra(shipments)
    expected = [
        ['IN', 'US', 8],
        ['IN', 'CA', 3],
    ]
    assert result == expected

def test_collect_pairs(example_shipments):
    result = collect_pairs([
        ['US', 'IN', 14],
        ['US', 'CA', 17],
        ['IN', 'US', 3],
        ['CA', 'US', 4],
    ])
    expected = [
        ['US', 'CA', 17, 4],
        ['US', 'IN', 14, 3],
    ]
    assert result == expected