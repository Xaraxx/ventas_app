
import click


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@clients.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    pass


@clients.command()
@clients.pass_context
def update(ctx, client_uid):
    """Updates the client information"""
    pass


@clients.command()
@clients.pass_context
def delete(ctx, client_uid):
    """Delete the client information"""
    pass


@clients.command()
@clients.pass_context
def clients_list(ctx):
    """List all clients"""
    pass

all = clients

