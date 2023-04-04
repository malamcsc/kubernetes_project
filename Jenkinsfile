pipeline {
    agent any
	
	environment {
				PROJECT_ID = 'kubernetes-project-378913'
                CLUSTER_NAME = 'jenkin-cluster'
                LOCATION = 'asia-east1-a'
                CREDENTIALS_ID = 'kubernetes'
				DOCKERHUB_CREDENTIALS = credentials('dockerhub')
			}
	
    stages {
		stage('Checkout Source') {
      		steps {
        		git url:'https://github.com/malamcsc/kubernetes_project.git', branch:'master', credentialsId: 'github'
      		}
    	}
	    
	    stage("Build image") {
            steps {
                script {
                    myapp = docker.build("gcr.io/kubernetes-project-378913/k8s_flask_image:${env.BUILD_ID}")
                }
            }
        }
	    
	    stage('Login and Dcoker push') {
          steps {
            script{
                  withCredentials([file(credentialsId: "gcloud-cred", variable: "GCLOUD_CRED")]){
                  sh ''' docker push malamcsc/kubernetes_project:${env.BUILD_ID} --key-file="$GCLOUD_CRED"} '''
                  }
		        }
           }
	    
	    stage('Deploy to K8s') {
		    steps{
			    echo "Deployment started ..."
				sh "sed -i 's/tagversion/${env.BUILD_ID}/g' deployment.yaml"
			    step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
			    echo "Deployment Finished ..."
		    }
	    }
    }
}