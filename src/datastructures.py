
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    # Genera un ID aleatorio
    def _generateId(self):
        return randint(0, 99999999)

    # -------------------------
    # Agregar un miembro
    # -------------------------
    def add_member(self, member):
        # si no viene id, generamos uno
        if "id" not in member:
            member["id"] = self._generateId()

        # asegurarse de que el apellido sea siempre el de la familia
        member["last_name"] = self.last_name

        self._members.append(member)
        return member

    # -------------------------
    # Eliminar un miembro por id
    # -------------------------
    def delete_member(self, id):
        for i, m in enumerate(self._members):
            if m["id"] == id:
                del self._members[i]
                return True
        return False

    # -------------------------
    # Obtener un miembro por id
    # -------------------------
    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    # -------------------------
    # Actualizar un miembro
    # -------------------------
    def update_member(self, id, updates):
        for i, m in enumerate(self._members):
            if m["id"] == id:
                # actualizar solo los campos que vienen en updates
                self._members[i].update(updates)
                # asegurarnos de que el apellido no cambie
                self._members[i]["last_name"] = self.last_name
                return self._members[i]
        return None

    # -------------------------
    # Obtener todos los miembros
    # -------------------------
    def get_all_members(self):
        return self._members