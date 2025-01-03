import fsb5
import os

error_log_path = os.path.join(os.getcwd(), 'failedConversions.txt')

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:

        if file.endswith('.fsb'):
            fsb_path = os.path.join(root, file)
            with open(fsb_path, 'rb') as f:
                fsb = fsb5.FSB5(f.read())

            print("=====================================")
            print(f"Processing {fsb_path}")
            print(fsb.header)
            print("=====================================")
            ext = fsb.get_sample_extension()

            for sample in fsb.samples:
                try:

                    print("=====================================")
                    print('''\t{sample.name}.{extension}:
                    Frequency: {sample.frequency}
                    Channels: {sample.channels}
                    Samples: {sample.samples}
                    Metadata: {sample.metadata}
                    '''.format(sample=sample, extension=ext))
                    print("=====================================")

                    parent_dir = os.path.dirname(root)

                    output_dir = os.path.join(parent_dir, "output")
                    bankoutput_dir = os.path.join(output_dir, file[:-4])


                    os.makedirs(bankoutput_dir, exist_ok=True)
                    with open(os.path.join(bankoutput_dir, f'{sample.name}.{ext}'), 'wb') as f:
                        rebuilt_sample = fsb.rebuild_sample(sample)
                        f.write(rebuilt_sample)
                except OSError as e:
                    print("=====================================")
                    print(f"Error processing {sample.name}:")
                    print(e)
                    print("=====================================")
                    with open(error_log_path, 'a') as error_log:
                        error_log.write(f"Error processing {sample.name} in {fsb_path}:\n{e}\n")