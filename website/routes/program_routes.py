from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models.programs import Program
from website import MySQL
from flask import jsonify

program_bp = Blueprint('program_bp', __name__)
mysql = MySQL()

@program_bp.route('/add', methods=['GET', 'POST'])
def add_program():
    if request.method == 'POST':
        code = request.form['programcode']
        name = request.form['programname']
        college_code = request.form['collegecode']

        Program.add_program(mysql, code, name, college_code)
        flash('Program Added Successfully', 'success')
        return redirect(url_for('program_bp.programs_list'))

    return render_template("Program Template/programs.html")

@program_bp.route('/programs')
def programs_list():
    programs = Program.get_all_programs(mysql)
    return render_template('Program Template/programs.html', programs=programs)

@program_bp.route('/update', methods=['POST'])
def update_program():
    code = request.form['programcode']
    name = request.form['programname']
    college_code = request.form['collegecode']
    
    Program.update_program(mysql, code, name, college_code)
    flash('Program Updated Successfully', 'success')
    return redirect(url_for('program_bp.programs_list'))

@program_bp.route('/program/<string:code>')
def search_program(code):
    program = Program.search_program(mysql, code)
    
    if program:
        return jsonify({
            'code': program.code,
            'name': program.name,
            'college_code': program.college_code
        })
    return jsonify(None)
    
    
