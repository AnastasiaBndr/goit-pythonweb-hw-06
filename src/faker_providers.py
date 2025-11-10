from faker.providers import DynamicProvider

disciplines_provider = DynamicProvider(
    provider_name="disciplines",
    elements=["Math", "Computer Architecture", "Physics",
              "History", "English", "Object-Oriented Programming", "Program Analysis", "Testing", "Cloud computing"],
)

