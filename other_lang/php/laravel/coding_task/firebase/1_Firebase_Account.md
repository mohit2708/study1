### Firebase Account
#### How to Create a Firebase Account (Step-by-Step)
- **Open the Firebase website:** https://firebase.google.com/
- Click “Get Started”
- Login With Google Account
- Create a New Project
  - Click "Add project"
  - Enter your project name
  - Example: my-laravel-app
  - You can disable Google Analytics (optional)
  - Click Create project
- After Project is Created → Open Firebase Console
  - Click Continue to enter the console.
- 🚀 Firebase Account is Now Created

#### Enable Cloud Messaging (Required for Push Notification)
- Inside your Firebase project:
- Go to “Project Settings” :- (bottom left gear icon)
- Click “Cloud Messaging” tab
  - Here you will find:
    - Server Key (FCM key)
    - Sender ID
- Laravel will use the service account JSON, not the server key.

#### Generate Service Account JSON
- Steps:
  - Console → Project Settings
  - Tab → Service accounts
  - Click “Generate new private key”
  - A service-account.json file will download
- You will need to place this file in:
  - create the downloaded file rename - downloaded_or_rename_file_name
  - and **create the folder** firebase inside the **/storage/app**
  - The path in .env must match exact filename

```php
/storage/app/firebase/downloaded_or_rename_file_name.json
```

#### After creating folder → Add in .env
```php
# Replace /full/path/to/ with the actual path where your serviceAccountKey.json is located.
FIREBASE_CREDENTIALS=/storage/app/firebase/service-account.json
```