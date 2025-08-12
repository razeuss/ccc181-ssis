from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from website.models.programs import Program
from website.models.college import College
from website import MySQL

program_bp = Blueprint('program_bp', __name__)
college_bp = Blueprint('college_bp', __name__)
mysql = MySQL()

@program_bp.route('/addprog', methods=['GET', 'POST'])
def add_program():
    if request.method == 'POST':
        code = request.form['programcode']
        name = request.form['programname']
        college_code = request.form['college_code']

        existing_program = Program.get_program_by_code(mysql, code)
        if existing_program:
            flash('Program already exists.', 'error')
            return redirect(url_for('program_bp.programs_list'))

        Program.add_program(mysql, code, name, college_code)
        flash('Program Added Successfully', 'success')
        return redirect(url_for('program_bp.programs_list'))

  
    colleges = College.get_all_collegecodes(mysql)
    return render_template("Program Template/programs.html", colleges=colleges)


@program_bp.route('/programs')
def programs_list():
    programs = Program.get_all_programs(mysql)
    colleges = College.get_all_collegecodes(mysql)
    return render_template('Program Template/programs.html', programs=programs, colleges=colleges)

@program_bp.route('/update/<string:program_code>', methods=['GET', 'POST'])
def update_program(program_code):
    if request.method == 'POST':
        new_code = request.form['programcode']  # Updated program code
        name = request.form['programname']
        college_code = request.form['college_code']

        # Update the program with the new code and details
        Program.update_program(mysql, program_code, new_code, name, college_code)
        flash('Program Updated Successfully', 'success')
        return redirect(url_for('program_bp.programs_list'))

    program = Program.search_program(mysql, program_code)
    return render_template('Program Template/edit_program.html', program=program)

@program_bp.route('/deleteprog/<string:code>', methods=['POST'])
def delete_program(code):
    Program.delete_program(mysql, code)
    flash('Program Deleted Successfully', 'success')
    return redirect(url_for('program_bp.programs_list'))

@program_bp.route('/program', methods=['GET'])
def search_program():
    query = request.args.get('query')
    
    program_by_code = Program.search_program(mysql, query)
    if program_by_code:
        return jsonify({
            'code': program_by_code.code,          # Accessing the properties of Program object
            'name': program_by_code.name,
            'college_code': program_by_code.college_code,
        })
        
    program_by_name = Program.search_program_by_name(mysql, query)
    if program_by_name:
        return jsonify({
            'code': program_by_name[0],
            'name': program_by_name[1],
            'college_code': program_by_name[2],
        })
        
    return jsonify(None)

@program_bp.route('/filter', methods=['GET'])
def filter_programs():
    college_code = request.args.get('college_code', 'all')  # default is 'all'
    
    if college_code != 'all':
        programs = Program.filter_programs(mysql, college_code)
    else:
        programs = Program.get_all_programs(mysql)

    colleges = College.get_all_collegecodes(mysql)

    if not programs:
        flash('No programs found for this college', 'warning')

    return render_template(
        'Program Template/programs.html',
        programs=programs,
        colleges=colleges,
        selected_college=college_code
    )


