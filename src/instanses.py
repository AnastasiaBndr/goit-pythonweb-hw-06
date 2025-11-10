from .models import Group, Student, Teacher, Discipline, Grade


MODELS = {
    "Group": Group,
    "Student": Student,
    "Teacher": Teacher,
    "Discipline": Discipline,
    "Grade": Grade,
}


def create_instance(session, model_name, **kwargs):
    model = MODELS.get(model_name)
    if not model:
        print(f"Model '{model_name}' doesn`t found.")
        return

    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    print(f"✅ Created {model_name}: {instance}")


def list_instances(session, model_name):
    model = MODELS.get(model_name)
    if not model:
        print(f"Model '{model_name}' doesn`t found.")
        return

    records = session.query(model).all()
    if not records:
        print(f"⚠️ No data for {model_name} was found.")
        return

    for r in records:
        print(r)


def update_instance(session, model_name, record_id, **kwargs):
    model = MODELS.get(model_name)
    if not model:
        print(f"Model '{model_name}' doesn`t found.")
        return

    instance = session.get(model, record_id)
    if not instance:
        print(f"❌ Object {model_name} with id={record_id} doesn`t found.")
        return

    for key, value in kwargs.items():
        if hasattr(instance, key) and value is not None:
            setattr(instance, key, value)

    session.commit()
    print(f"✅ Updated {model_name} (id={record_id})")


def delete_instance(session, model_name, record_id):
    model = MODELS.get(model_name)
    if not model:
        print(f"Model '{model_name}' doesn`t found.")
        return

    instance = session.get(model, record_id)
    if not instance:
        print(f"❌ Object {model_name} with id={record_id} doesn`t found.")
        return

    session.delete(instance)
    session.commit()
    print(f"🗑 Deleted {model_name} with id={record_id}")


