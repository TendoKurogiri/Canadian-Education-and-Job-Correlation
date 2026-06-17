import pandas as pd

def convert_all_raw_to_base():
    """
    Reads the original sample data, applies the FULL NGS Class of 2020 Data Dictionary 
    mapping to rename ALL 100+ cryptic columns to human-readable names, 
    and saves the complete base dataset.
    """
    print("Loading original sample dataset...")
    
    try:
        # Load your original raw sample file
        df = pd.read_csv('../data/raw/Original sample.csv')
    except FileNotFoundError:
        print("Error: Could not find 'Original sample.csv' in the '../data/raw/' folder.")
        return

    # FULL Data Dictionary Mapping
    # Extracted from the National Graduates Survey (Class of 2020) PUMF Dictionary
    # Key columns for your analysis are mapped to match your existing scripts perfectly.
    data_dictionary = {
        'PUMFID': 'Randomly generated record identifier for the PUMF file',
        'CERTLEVP': 'Level of Study Grouping', # Custom mapped for your script
        'REG_INST': 'Region of Postsecondary Institution', # Custom mapped for your script
        'REG_RESP': 'Time of interview 2023 - Region of primary residence',
        'PGMCIPAP': 'Program Fields of Study', # Custom mapped for your script
        'PGM_P034': '2020 Program - Full-time or part-time student',
        'PGM_P036': '2020 Program - Reason did not take program full-time',
        'PGM_P100': 'Work placement during program',
        'PGM_P111': 'Work placement during prog - Description',
        'PGM_280A': 'Entrepreneurial skills - Started a business',
        'PGM_280B': 'Entrepreneurial skills - Completed courses',
        'PGM_280C': 'Entrepreneurial skills - Business plan or pitch competition',
        'PGM_280D': 'Entrepreneurial skills - Visited an entrepreneurship centre',
        'PGM_280E': 'Entrepreneurial skills - Worked on an entrepreneurship project',
        'PGM_280F': 'Entrepreneurial skills - None of the above',
        'PGM_290': '2020 Program - Worked during program',
        'PGM_350': '2020 Program - Volunteer activities during program',
        'PGM_380': '2020 Program - Components taken outside of Canada',
        'PGM_P401': '2020 Program - Online or distance education',
        'PGM_410': '2020 Program - Main factor in choice of postsecondary institution',
        'PGM_415': '2020 Program - Main factor in choice of program',
        'PGM_430': '2020 Program - Choose the same field of study or specialization again',
        'COV_010': 'COVID-19 - Completion of program delayed',
        'COV_070': 'COVID-19 - Plans for further postsecondary education changed',
        'COV_080': 'COVID-19 - Employment status/plans affected',
        'EDU_010': 'After 2020 program - Other postsecondary programs taken',
        'EDU_P020': 'After 2020 program - Number of other programs taken',
        'HLOSINTP': 'Time of interview 2023 - Aggregated highest level of ed. completed',
        'STL_010': 'Government-student loan program - Applied',
        'STL_020': 'Government-student loan program - Applications approved',
        'STULOANS': 'Government-student loan program - Received',
        'STL_030': 'Government-student loan program - Main reason did not apply',
        'OWESLGD': 'Government-student loan program - Debt size - Graduation 2020',
        'OWEGVIN': 'Government-student loan program - Debt size - Interview 2023',
        'STL_080': 'Government-student loan program - Remission/debt reduction/loan forg.',
        'STL_100A': 'Received government assistance: Repayment assistance plan',
        'STL_100B': 'Received government assistance: Revision of terms',
        'STL_100C': 'Received government assistance: Interest only payments',
        'STL_100D': 'Received government assistance: None of the above',
        'STL_130': 'Government-student loan program - Total repayment term',
        'STL_150': 'Government-student loan program - Repaymt of loan from financial inst.',
        'STL_160B': 'Sources of funding - RESP',
        'STL_160C': 'Sources of funding - Government grants or bursaries',
        'STL_160D': 'Sources of funding - Non-government grants or bursaries',
        'STL_160E': 'Sources of funding - Scholarships or awards',
        'STL_160F': 'Sources of funding - Employment earnings or savings',
        'STL_160G': 'Sources of funding - Research or teaching assistantship',
        'STL_160H': 'Sources of funding - Parents, family, friends',
        'STL_160I': 'Sources of funding - Bank or institution loans',
        'STL_160J': 'Sources of funding - Credit cards',
        'STL_160L': 'Sources of funding - Employer',
        'STLP160N': 'Sources of funding - Other',
        'SRCFUND': 'Sources of funding - Number of sources - All postsecondary edu',
        'STL_170A': 'Main source of funding - Government student loans',
        'STL_170B': 'Main source of funding - RESP',
        'STL_170C': 'Main source of funding - Government grants or bursaries',
        'STL_170D': 'Main source of funding - Non-government grants or bursaries',
        'STL_170E': 'Main source of funding - Scholarships or awards',
        'STL_170F': 'Main source of funding - Employment earnings or savings',
        'STL_170G': 'Main source of funding - Research or teaching assistantship',
        'STL_170H': 'Main source of funding - Parents, family, friends',
        'STL_170I': 'Main source of funding - Bank or institution loans',
        'STL_170J': 'Main source of funding - Credit cards',
        'STL_170L': 'Main source of funding - Employer',
        'STLP170N': 'Main source of funding - Other',
        'RESPP': 'RESP - Total amount received for postsecondary education',
        'STL_190': 'Repay loans from family or friends for education',
        'DBTOTGRD': 'Loans at graduation 2020 - Debt size of non-government loans (range)',
        'DBTALGRD': 'Loans at graduation 2020 - Debt size of all loans',
        'DBTOTINT': 'Time of interview 2023 - Debt size of non-government loans (range)',
        'DBTALINT': 'Time of interview 2023 - Debt size of all loan',
        'SCHOLARP': 'Total amount received from scholarships/awards/fellowships and prizes',
        'LMA_010': 'Reference week - Attended school, college, CEGEP or university',
        'LFSTATP': 'Employment Status', # Custom mapped for your script
        'LMA2_07': 'Reference week - More than one job or business',
        'LMA3_P01': 'Reference week - Employee or self-employed',
        'LFCINDP': 'Reference week - Sector for job',
        'LFCOCCP': 'Reference week - Broad occupational category for job',
        'LFWFTPTP': 'Reference week - Full-time or part-time status of job or business',
        'LMA6_05': 'Reference week - Job permanent or not permanent',
        'LMA6_08': 'Job Search Method', # Custom mapped for your script
        'JOBQLEVP': 'Reference week - Aggregated level of studies required to get job',
        'JOBQLGRD': 'Reference week - Qualification for job compared to 2020 program',
        'JOBQLINT': 'Reference week - Qualification job vs level of education',
        'LMA6_11': 'Reference week - Relatedness of job or business to 2020 program',
        'LMA6_12': 'Reference week - Qualification level for job',
        'LMA6_13A': 'Reference week - Satisfied with overall job',
        'LMA6_13B': 'Reference week - Satisfied with wage or salary of job',
        'LMA6_13C': 'Reference week - Satisfied with job security',
        'JOBINCP': 'Reference week - Annual wage or salary for job',
        'LMA6_15': 'After program 2020 - First job',
        'AFT_P010': 'After 2020 program - Number of jobs or businesses',
        'AFT_P020': 'After 2020 Program - Length of time until first job or business',
        'AFT_P040': 'After 2020 program - Employee or self-employed - 1st job or business',
        'AFT_050': 'After 2020 program - Full-time or part-time - 1st job or business',
        'AFT_070': 'After 2020 program - Permanent/not permanent - 1st job or business',
        'AFT_080': 'After 2020 program - Reason job not permanent - 1st job or business',
        'AFT_090': 'After 2020 program - Relatedness of 1st job/business to program',
        'BEF_P140': 'Before 2020 Program - Main activity during 12 months before',
        'BEF_160': 'Before 2020 program - Number of months of work experience',
        'PREVLEVP': 'Before 2020 program - Aggregated highest level of studies completed',
        'HLOSGRDP': '2020 Program - Highest level of education completed',
        'PAR1GRD': '2020 Program - Level of education compared to that of one parent',
        'PAR1INT': 'Time of interview 2023 - Level of education vs of one parent',
        'PAR2GRD': '2020 Program - Level of education vs of the other parent',
        'PAR2INT': 'Time of interview 2023 - Level of education vs that of other parent',
        'GRADAGEP': '2020 Program - Age at time of graduation - Grouping',
        'GENDER2': 'Gender', # Custom mapped for your script
        'MS_P01': 'Marital status',
        'MS_P02': 'Have any dependent children',
        'CTZSHIPP': 'Immigration Status', # Custom mapped for your script
        'VISBMINP': 'Self-identified as a member of a visible minority group',
        'PERSINCP': 'Total Personal Income in 2022', # Custom mapped for your script
        'DDIS_FL': 'Disability status',
        'WTPF': 'Survey weight',
        'VERDATE': 'Date of file creation'
    }

    # Rename the columns. We don't filter columns out anymore, 
    # so your final CSV will contain all 100+ original columns, but fully translated!
    df.rename(columns=data_dictionary, inplace=True)
    
    # Save the newly named data to become your base 'Education_and_Employment.csv'
    output_file = '../data/raw/Education_and_Employment.csv'
    df.to_csv(output_file, index=False)
    
    print(f"Success! Translated base data (with all columns preserved) saved to {output_file}")
    print("This file is now ready to be processed by 'data_manipulation_4.py'")

if __name__ == "__main__":
    convert_all_raw_to_base()