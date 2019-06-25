from student_directory import student_app


if __name__ == "__main__":
    student_app.run(debug=student_app.config.get('DEBUG'), threaded=student_app.config.get('THREADED'),
                    port=student_app.config.get('PORT'), host=student_app.config.get('HOST'))
