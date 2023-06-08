from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'

    name = fields.Char('Task Name', required=True)
    description = fields.Text('Task Description')
