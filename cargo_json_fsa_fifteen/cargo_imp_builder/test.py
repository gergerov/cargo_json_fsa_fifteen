import pykson
import json
import jinja2
from cargo_json_fsa_fifteen.cargo_imp_builder import templates as t


class CargoImpNode(pykson.JsonObject):
    """
    Имеющая ветви часть дерева спецификации
    """
    pass


class CargoImpLowNode(CargoImpNode):
    """
    Не имеющия ветвей часть дерева спецификации.
    Базовый метод > get_imp,
    который возвращает текст
    части грузового сообщения
    спецификации Cargo-IMP,
    которая не имеют вложенных частей.
    (нижний уровень дерева, конечные элементы ветви)
    При описании класса необходимо указывать
    связанный шаблон jinja2
    """

    def get_imp(self):
        """

        """
        self.dict = pykson.Pykson().to_dict_or_list(self)
        self.imp_string = self.template.render(self.dict)
        return self.imp_string


class StandartMessageIdentification(CargoImpLowNode):
    standart_message_identifier = pykson.StringField()
    message_type_version_number = pykson.StringField()
    template = t.standart_message_identification


class Message(CargoImpNode):
    standart_message_identification = pykson.ObjectField(StandartMessageIdentification)

    def get_imp(self):
        self.imp_node = self.standart_message_identification.get_imp()
        # self.imp_node += self.consignment_detail.get_imp()
        # и так далее
        return self.imp_node


smi_dict = {
    "standart_message_identification": {
        "standart_message_identifier": "FSA",
        "message_type_version_number": "15"
    }
}


smi_json = json.dumps(smi_dict)

smi_object = pykson.Pykson().from_json(smi_json, Message)
print(smi_object.get_imp())
# pykson.Pykson().
