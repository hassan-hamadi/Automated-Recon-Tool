import pytest

from main import validate_target


@pytest.mark.parametrize('domain', [
    'example.com',
    'sub.example.co.uk',
    'test-domain.org',
])
def test_validate_target_valid_domains(domain):
    assert validate_target(domain) is True


@pytest.mark.parametrize('ip', [
    '192.168.0.1',
    '10.0.0.255',
    '255.255.255.255',
])
def test_validate_target_valid_ips(ip):
    assert validate_target(ip) is True


@pytest.mark.parametrize('domain', [
    'example',           # missing TLD
    'invalid_domain',    # underscore not allowed
    'example..com',      # double dot
    'example com',       # space
])
def test_validate_target_invalid_domains(domain):
    assert validate_target(domain) is False


@pytest.mark.parametrize('ip', [
    '192.168.1',       # too few octets
    '192.168.1.1.1',   # too many octets
    '192.168.1.1a',    # trailing characters
    '10.0.0.',         # trailing dot
    '192.168..1',      # double dot
])
def test_validate_target_invalid_ips(ip):
    assert validate_target(ip) is False
