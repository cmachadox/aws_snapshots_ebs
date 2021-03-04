import boto3

ec2 = boto3.client('ec2')

def createSnapshot():
    volumes = ec2.describe_volumes()
    snapshots_created = 0
    
    for volume in volumes['Volumes']:
        try:
            
            instance_id = str(volume['Attachments'][0]['InstanceId'])
            tags = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['Tags']
            description = " meu snapshot de cada dia " + volume['VolumeId']
            backup = ""
            
            for tag in tags:
                if tag['Key'] == 'snapshot':
                    backup = tag['Value']

            print(description)
            if backup == 'yes':
                response = ec2.create_snapshot(
                    Description= description,
                    VolumeId=volume['VolumeId'],
                    DryRun=False
                )
                print(str(response['SnapshotId']),"criado")
                snapshots_created += 1
        except Exception as e:
            print("Error:", str(e))
            return snapshots_created

def handler(event, context):
    print("starting execution")
    snapshots_created = createSnapshot()
    return "Snapshots created = " + str(snapshots_created)
