pipeline {
  agent {
    docker {
      image 'python:3-alpine'
      args '-p 5000:5000'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'echo "build"'
      }
    }
  }
}