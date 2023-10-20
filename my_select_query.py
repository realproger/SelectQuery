class MySelectQuery:
    def __init__(self, csv_content):
        self.data = []
        lines = csv_content.split("\n")
        self.headers = lines[0].strip().split(",")

        for line in lines[1:]:
            if line.strip():
                values = line.strip().split(",")
                if len(values) == len(self.headers):
                    row = {}
                    for i, value in enumerate(values):
                        row[self.headers[i]] = value.strip()
                    self.data.append(row)

    def where(self, coloumn_name, criteria):
        result = []
        for row in self.data:
            if row[coloumn_name] == criteria:
                values = [row[h] for h in self.headers]
                result.append(",".join(values))
        return result

csv_content = """name,year_start,year_end,position,height,weight,birth_date,college
Alaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University
Zaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University
Kareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles'
Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University"""

query = MySelectQuery(csv_content)
# result = query.where(" name", " Andrew Brown")
# print(result)