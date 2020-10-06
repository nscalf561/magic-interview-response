import pandas as pd
from typing import Tuple


class WeatherStationStats():
    def __init__(self, csv_file='question_5/data.csv'):
        self.csv_file = csv_file

    def get_lowest_temp(self) -> Tuple[int, int]:
        """ This is the solution to part 1, returns the station_id and date as a tuple """
        try:
            df = pd.read_csv(self.csv_file)
            lowest_temp_row = df.iloc[df['temperature_c'].values.argmin()]
            return round(lowest_temp_row['station_id']), round(lowest_temp_row['date'], 3)
        except Exception as ex:
            print(f'Error getting lowest temperature in weather data: {ex}')
            raise

    def get_largest_fluctuations(self, df=None) -> int:
        """ This is the solution to part 2, returns the station_id """
        try:
            if df is None:
                df = pd.read_csv(self.csv_file)
            # highest fluctuation is a tuple of the station_id and the current variation for that station
            highest_fluctuation = (0, 0)
            # sum obj will be {station_id: (current_variance_sum, previous_value)}
            sum_obj = {}
            for index, row in df.iterrows():
                # Handle internal tracking of variance
                if row.station_id in sum_obj:
                    station_variance = sum_obj[row.station_id][0]
                    station_previous_temp = sum_obj[row.station_id][1]

                    station_variance = station_variance + abs(station_previous_temp - row.temperature_c)
                    sum_obj[row.station_id] = (station_variance, row.temperature_c)

                    # Handle tracking the current highest variance
                    if station_variance > highest_fluctuation[1]:
                        highest_fluctuation = (row.station_id, station_variance)
                else:
                    sum_obj[row.station_id] = (0, row.temperature_c)

            return round(highest_fluctuation[0])
            
        except Exception as ex:
            print(f'Error getting largest fluctuations in weather data: {ex}')
            raise
    
    def get_largest_fluctuations_by_date_range(self, start: str, end: str) -> int:
        """ This is the solution to part 3, returns the station_id """
        try:
            df = pd.read_csv(self.csv_file)
            df = df[df['date'].between(start, end)]
            return self.get_largest_fluctuations(df=df)
        except Exception as ex:
            print(f'Error getting largest fluctuations between two dates: {ex}')
            raise

# x=WeatherStationStats(csv_file='question_5/short_data.csv')
# y=x.get_largest_fluctuations_by_date_range(2004.042,2004.152)
# print(y)
