class Pain: 

    def __init__(self, id_pers : int, type : str):
        self.id_pers = id_pers
        self.type = type

    def __repr__(self):
        return str(self.id_pers) + "type : " + self.type