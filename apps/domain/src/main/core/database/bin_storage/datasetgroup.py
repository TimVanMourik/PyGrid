from .. import BaseModel, db


class JsonObject(BaseModel):
    __bind_key__ = "bin_store"
    __tablename__ = "json_object"

    id = db.Column(db.String(255), primary_key=True)
    binary = db.Column(db.JSON())

    def __str__(self):
        return f"<JsonObject id: {self.id}>"


class DatasetGroup(BaseModel):
    __tablename__ = "datasetgroup"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    bin_object = db.Column(db.String(255), db.ForeignKey("bin_object.id"))
    dataset = db.Column(db.String(255), db.ForeignKey("json_object.id"))

    def __str__(self):
        return (
            f"<DatasetGroup id: {self.id}, bin_object: {self.bin_object}, "
            f"dataset: {self.dataset}>"
        )
