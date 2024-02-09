from flask import Flask, render_template, request, redirect, url_for, send_from_directory

webportfolio = Flask(__name__)


@webportfolio.route('/')
def index():
#
#     # default language for my website
#     lang = 'en'
#
    return redirect(url_for('landingpage.html'))


# @webportfolio.route('/landingpage', methods=['POST', 'GET'])
# def landing():
#
#     # default language for my website
#     lang = 'en'
#
#     return render_template('/templates/landingpage.html')


# @webportfolio.route('/landingpage/items', methods=['POST', 'GET'])

# def items():
#
#     # default language for my website
#     lang = 'en'
#
#     return render_template('/templates/index.html')


# @webportfolio.route('/landingpage/new', methods=['POST', 'GET'])
# #
# def new():
#
#     return render_template('/landingpage/templates/about_me.html')
# # redirect(url_for('landingpage'))


if __name__ == '__main__':
    webportfolio.run()