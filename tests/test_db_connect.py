from unittest.mock import patch, MagicMock
from src.db.db_connect import get_engine


def test_get_engine_returns_engine():
    with patch("src.db.db_connect.create_engine") as mock_create:
        mock_create.return_value = MagicMock()
        engine = get_engine()
        assert engine is not None
        mock_create.assert_called_once()
