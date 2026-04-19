@app.route('/result7', methods=['GET', 'POST'])
def result7():
    res = None
    
    if request.method == 'POST':
        date = request.form.get('date', '').strip()
        email = request.form.get('email', '').strip()

        if date and '@' in email:
            res = [date, email]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result7.html', res=res)
