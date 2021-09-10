        def func_for_both_or(x):
            if np.isnan(x[3]):
                converted_data = cashflow_csv_ndarray[
                    np.where(
                        (cashflow_csv_ndarray[:, 8] == x[2]) & (cashflow_csv_ndarray[:, 9] == 1),
                        True, False)]
                res_preservation_data = cashflow_csv_ndarray[
                    np.where((cashflow_csv_ndarray[:, 8] == int(x[4])) & (
                            cashflow_csv_ndarray[:, 9] == 0), True, False)]
                if np.sum(converted_data[:, 14], axis=0) + np.sum(res_preservation_data[:, 14], axis=0) == 0:
                    return True
                else:
                    return False
            elif np.isnan(x[4]):
                converted_data = cashflow_csv_ndarray[
                    np.where(
                        (cashflow_csv_ndarray[:, 8] == x[2]) & (cashflow_csv_ndarray[:, 9] == 0),
                        True, False)]

                pay_preservation_data = cashflow_csv_ndarray[
                    np.where((cashflow_csv_ndarray[:, 8] == int(x[3])) & (
                            cashflow_csv_ndarray[:, 9] == 1), True, False)]
                if np.sum(converted_data[:, 14], axis=0) + np.sum(pay_preservation_data[:, 14], axis=0) == 0:
                    return True
                else:
                    return False
            else:
                converted_data_0 = cashflow_csv_ndarray[
                    np.where(
                        (cashflow_csv_ndarray[:, 8] == x[2]) & (cashflow_csv_ndarray[:, 9] == 0),
                        True, False)]

                converted_data_1 = cashflow_csv_ndarray[
                    np.where(
                        (cashflow_csv_ndarray[:, 8] == x[2]) & (cashflow_csv_ndarray[:, 9] == 1),
                        True, False)]

                pay_preservation_data = cashflow_csv_ndarray[
                    np.where((cashflow_csv_ndarray[:, 8] == int(x[3])) & (
                            cashflow_csv_ndarray[:, 9] == 1), True, False)]

                res_preservation_data = cashflow_csv_ndarray[
                    np.where((cashflow_csv_ndarray[:, 8] == int(x[4])) & (
                            cashflow_csv_ndarray[:, 9] == 0), True, False)]
                if np.sum(converted_data_0[:, 14], axis=0) + np.sum(pay_preservation_data[:, 14], axis=0) == 0 & np.sum(
                        converted_data_1[:, 14], axis=0) + np.sum(res_preservation_data[:, 14], axis=0):
                    return True
                else:
                    return False
                  
      unmatched = both_or_conversion_ndarray[~np.array(check_result)]
            data = []
            for one in unmatched:
                if not np.isnan(one[4]):
                    res_preservation_data = cashflow_csv_ndarray[
                        np.where((cashflow_csv_ndarray[:, 8] == int(one[4])), True, False) & (
                                cashflow_csv_ndarray[:, 9] == 0)]

                    converted_data = cashflow_csv_ndarray[
                        np.where(
                            (cashflow_csv_ndarray[:, 8] == one[2]) & (cashflow_csv_ndarray[:, 9] == 1),
                            True, False)]
                    re = np.where((converted_data[:, 10] == res_preservation_data[:, 10]), True, False) & (
                            converted_data[:, 14] + res_preservation_data[:, 14] != 0)
                    if len(data):
                        new_data = np.concatenate([converted_data[re], res_preservation_data[re]], axis=0)
                        reorder = [rv for r in
                                   zip(range(0, len(new_data) // 2), range(len(new_data) // 2, len(new_data)))
                                   for rv in
                                   r]
                        new_data = new_data[reorder, :]
                        data = np.concatenate([data, new_data], axis=0)
                    else:
                        data = np.concatenate([converted_data[re], res_preservation_data[re]], axis=0)
                        reorder = [rv for r in zip(range(0, len(data) // 2), range(len(data) // 2, len(data))) for rv in
                                   r]
                        data = data[reorder, :]

                if not np.isnan(one[3]):
                    pay_preservation_data = cashflow_csv_ndarray[
                        np.where((cashflow_csv_ndarray[:, 8] == int(one[3])), True, False) & (
                                cashflow_csv_ndarray[:, 9] == 1)]
                    converted_data = cashflow_csv_ndarray[
                        np.where(
                            (cashflow_csv_ndarray[:, 8] == one[2]) & (cashflow_csv_ndarray[:, 9] == 0),
                            True, False)]
                    re = np.where((converted_data[:, 10] == pay_preservation_data[:, 10]), True, False) & (
                            converted_data[:, 14] + pay_preservation_data[:, 14] != 0)
                    if len(data):
                        new_data = np.concatenate([converted_data[re], pay_preservation_data[re]], axis=0)
                        reorder = [rv for r in
                                   zip(range(0, len(new_data) // 2), range(len(new_data) // 2, len(new_data)))
                                   for rv in
                                   r]
                        new_data = new_data[reorder, :]
                        data = np.concatenate([data, new_data], axis=0)
                    else:
                        data = np.concatenate([converted_data[re], pay_preservation_data[re]], axis=0)
                        reorder = [rv for r in zip(range(0, len(data) // 2), range(len(data) // 2, len(data))) for rv in
                                   r]
                        data = data[reorder, :]

            unmatched_data = pd.DataFrame(data, columns=cashflow_csv.columns.tolist())
            unmatched_data = pd.concat([unmatched_data, ], axis=0, ignore_index=True)  
