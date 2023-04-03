pipeline {
    agent any
	
	environment {
				PROJECT_ID = 'kubernetes-project-378913'
                CLUSTER_NAME = 'jenkin-cluster'
                LOCATION = 'asia-east1-a'
                CREDENTIALS_ID = 'kubernetes'
				DOCKERHUB_CREDENTIALS = credentials('dockerhub')
				BUILD_ID = 2	
			}
	
    stages {
		stage('Checkout Source') {
      		steps {
        		git url:'https://github.com/malamcsc/kubernetes_project.git', branch:'master', credentialsId: 'github'
      		}
    	}
	    
	    // stage("Build image") {
        //     steps {
        //         script {
        //             myapp = docker.build("malamcsc/kubernetes_project:${env.BUILD_ID}")
        //         }
        //     }
        // }
	    
	    // stage('Login and Dcoker push') {
        //   steps {
        //     script{
        //           withDockerRegistry([ credentialsId: "dockerhub", url: "" ]){
        //           myapp.push("${env.BUILD_ID}")}
        //           }
		//         }
        //    }
	    
	    stage('Deploy to K8s') {
		    steps{
			    echo "Deployment started ..."
			    sh 'ls -ltr'
			    sh 'pwd'
				sh "sed -i 's/tagversion/${env.BUILD_ID}/g' simple_flask.yaml"
			    echo "Start deployment of deployment.yaml"
			    step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'simple_flask.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
			    echo "Deployment Finished ..."
		    }
	    }
    }
}