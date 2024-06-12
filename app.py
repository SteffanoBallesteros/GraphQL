
from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Definición del esquema
class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return "Hola, mundo!"

schema = graphene.Schema(query=Query)

# Configuración de la aplicación Flask
app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
