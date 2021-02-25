import twint


c = twint.Config()
c.Search = "#ditchthemask"
c.Lang = "en"
c.Limit = 1_000_000
c.Since = "2020-01-01"
c.Until = "2020-10-31"
c.Store_json = True
c.Output = "../raw data/ditchthemask + 2020-01 - 2020-10-31.json"

twint.run.Search(c)
