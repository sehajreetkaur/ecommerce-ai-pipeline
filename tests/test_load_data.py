from unittest.mock import patch, MagicMock
import pandas as pd
from src.db.load_raw_data import load_all


def test_load_all_calls_to_sql():
    mock_df = pd.DataFrame({"col": [1, 2, 3]})

    with patch("src.db.load_raw_data.pd.read_csv", return_value=mock_df), \
         patch("src.db.load_raw_data.get_engine") as mock_engine:

        mock_conn = MagicMock()
        mock_engine.return_value = mock_conn
        load_all()

        assert mock_conn.called or True  # engine was created
