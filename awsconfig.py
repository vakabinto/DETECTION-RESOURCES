import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')
    
    # Get a list of all EC2 instances
    instances = ec2.describe_instances()['Reservations']
    
    for reservation in instances:
        for instance_info in reservation['Instances']:
            instance_id = instance_info['InstanceId']
            monitoring_enabled = instance_info['Monitoring']['State']
            
            if monitoring_enabled:
                print(f"Monitoring is enabled for EC2 instance: {instance_id}")
                # You can add more actions here, such as sending notifications or taking further steps.
            else:
                print(f"Monitoring is not enabled for EC2 instance: {instance_id}")