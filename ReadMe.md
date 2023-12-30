# Ownsite

Ownsite is a Django-based web application that acts as a  developer's portfolio.

## Features

- Allows the developer to act as admin 
    -can posts blogs, projects
    -services he/she he offers
- allows the developer to show his work.
- forms for contacting the developer

## Getting Started

### Prerequisites

- Python (version 3.x recommended)
- Django (version 3.x recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Phyb1/Ownsite.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ownsite
    ``

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ``
6. Access the application in your web browser at `http://127.0.0.1:8000/`.

### Usage

1. users visits the home view and sees a list of services with lins to more info on each and order making.
2. Visit the About page to seec ontact info and lins to social media
3. Visit the projects link to see pass projects the developer has worked on
 

### Testing

Run the tests using the following command:

```bash
python manage.py test
