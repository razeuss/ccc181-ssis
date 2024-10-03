from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models.programs import Program
from website import MySQL
from flask import jsonify

program_bp = Blueprint('program_bp', __name__)
mysql = MySQL()

@program_bp.route('/addprog', methods=['GET', 'POST'])
def add_program():
    if request.method == 'POST':
        code = request.form['programcode']
        name = request.form['programname']
        college_code = request.form['college_code']

        Program.add_program(mysql, code, name, college_code)
        flash('Program Added Successfully', 'success')
        return redirect(url_for('program_bp.programs_list'))

    return render_template("Program Template/programs.html")

@program_bp.route('/programs')
def programs_list():
    programs = Program.get_all_programs(mysql)
    return render_template('Program Template/programs.html', programs=programs)

@program_bp.route('/update/<string:program_code>', methods=['GET', 'POST'])
def update_program(program_code):
    if request.method == 'POST':
        name = request.form['programname']
        college_code = request.form['college_code']
        Program.update_program(mysql, program_code, name, college_code)
        flash('Program Updated Successfully', 'success')
        return redirect(url_for('program_bp.programs_list'))

    program = Program.search_program(mysql, program_code)
    return render_template('Program Template/edit_program.html', program=program)

@program_bp.route('/deleteprog/<string:code>', methods=['POST'])
def delete_program(code):
    Program.delete_program(mysql, code)
    flash('Program Deleted Successfully', 'success')
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


